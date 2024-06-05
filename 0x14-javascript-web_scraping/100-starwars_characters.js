#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  const characterPromises = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  });

  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error:', error);
    });
});

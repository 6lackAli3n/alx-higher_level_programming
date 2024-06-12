// using JQuery API fetch and list for all movies
// using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json

const url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  const films = data.results;
  for (const film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});

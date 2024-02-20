#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  printCharacters(data.characters, 0);
});

function printCharacters(characters, i) {
  if (i >= characters.length) {
    return;
  }
  request(characters[i], function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    printCharacters(characters, i + 1);
  });
}

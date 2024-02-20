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
  data.characters.forEach(function(characterUrl) {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

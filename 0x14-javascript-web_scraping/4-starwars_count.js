#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < data.results.length; i++) {
    const str = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;
    if (data.results[i].characters.includes(str)) {
      count++;
    }
  }
  console.log(count);
});

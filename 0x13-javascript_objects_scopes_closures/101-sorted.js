#!/usr/bin/node

const data = require('./101-data.js').dict;
const newData = {};
for (const i in data) {
  if (newData[data[i]] === undefined) {
    newData[data[i]] = [i];
  } else {
    newData[data[i]].push(i);
  }
}
console.log(newData);

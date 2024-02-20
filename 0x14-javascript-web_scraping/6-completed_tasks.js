#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const tasks = JSON.parse(body);
  const completedTasks = {};

  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed) {
      if (completedTasks[tasks[i].userId]) {
        completedTasks[tasks[i].userId]++;
      } else {
        completedTasks[tasks[i].userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});

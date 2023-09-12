#!/usr/bin/node

const fs = require('fs');
const x = fs.readFileSync(process.argv[2], 'uft8');
const y = fs.readFileSync(process.argv[3], 'uft8');
fs.writeFileSync(process.argv[4], x + y);

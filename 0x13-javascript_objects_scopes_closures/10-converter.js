#!/usr/bin/node

exports.converter = function (base) { return function (el) { return el.toString(base); }; };

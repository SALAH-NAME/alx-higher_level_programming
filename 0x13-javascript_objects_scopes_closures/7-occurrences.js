#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.map((x) => {
    if (x === searchElement) {
      count++;
      return 1;
    } else {
      return 0;
    }
  }
  );
  return count;
};

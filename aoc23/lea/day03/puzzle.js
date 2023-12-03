const { readDataAsLine } = require("../../../aoc21/lea/util");
const assert = require("assert");

function is_numeric(s) {
  return !isNaN(s - parseFloat(s));
}

const isSymbol = (str) => {
  return !is_numeric(str) && str !== ".";
};

assert.equal(isSymbol("."), false);
assert.equal(isSymbol("123456789"), false);
assert.equal(isSymbol("!"), true);
assert.equal(isSymbol("#"), true);

const isStar = (str) => {
  return str === "*";
};

const findNeighbor = (currentIndex, input, i, predicate) => {
  const directions = [
    [0, 1],
    [-1, -1],
    [0, -1],
    [1, 0],
    [-1, 0],
    [1, 1],
    [1, -1],
    [-1, 1],
  ];

  for (const [di, dj] of directions) {
    const ni = i + di;
    const nj = currentIndex + dj;

    if (
      ni >= 0 &&
      ni < input.length &&
      nj >= 0 &&
      nj < input[ni].length &&
      predicate(input[ni][nj])
    ) {
      return { i: ni, j: nj };
    }
  }

  return undefined;
};

const getStarIndex = (currentIndex, input, i) =>
  findNeighbor(currentIndex, input, i, isStar);

assert.equal(getStarIndex(2, ["123*.."], 0).i, 0);
assert.equal(getStarIndex(2, ["123*.."], 0).j, 3);
assert.equal(getStarIndex(6, ["..35..633.", "......#..."], 0), undefined);
assert.equal(getStarIndex(4, [".....*.58.", "..592....."], 1).i, 0);
assert.equal(getStarIndex(4, [".....*.58.", "..592....."], 1).j, 5);

const hasSymbol = (currentIndex, input, i) =>
  !!findNeighbor(currentIndex, input, i, isSymbol);

assert.equal(hasSymbol(0, ["123..."], 0), false);
assert.equal(hasSymbol(2, ["123%.."], 0), true);
assert.equal(hasSymbol(2, ["123...", "12*..."], 0), true);
assert.equal(hasSymbol(0, ["123...", "#23..."], 0), true);
assert.equal(hasSymbol(6, ["..35..633.", "......#..."], 0), true);
assert.equal(hasSymbol(4, [".....+.58.", "..592....."], 1), true);
assert.equal(hasSymbol(6, ["......755.", "...$.*...."], 0), true);

const part1 = () => {
  const input = readDataAsLine("./input.txt");
  const numbers = [];

  for (let i = 0; i < input.length; i++) {
    let indices = [];

    for (let j = 0; j < input[i].length; j++) {
      if (is_numeric(input[i][j])) {
        indices.push(j);
      }

      if (
        (j === input[i].length - 1 && indices.length > 0) ||
        (!is_numeric(input[i][j]) && indices.length > 0)
      ) {
        let number = "";
        let symbol = undefined;

        for (let k = 0; k < indices.length; k++) {
          number += input[i][indices[k]];
          if (!symbol) {
            symbol = hasSymbol(indices[k], input, i);
          }
        }

        const res = parseInt(number);

        if (symbol) {
          numbers.push(res);
        }
        indices = [];
      }
    }
  }

  return numbers.reduce((acc, number) => acc + number, 0);
};

const part2 = () => {
  const input = readDataAsLine("./input.txt");
  const numbers = new Map();

  for (let i = 0; i < input.length; i++) {
    let indices = [];

    for (let j = 0; j < input[i].length; j++) {
      if (is_numeric(input[i][j])) {
        indices.push(j);
      }

      if (
        (j === input[i].length - 1 && indices.length > 0) ||
        (!is_numeric(input[i][j]) && indices.length > 0)
      ) {
        let number = "";
        let starIndex = undefined;

        for (let k = 0; k < indices.length; k++) {
          number += input[i][indices[k]];
          if (!starIndex) {
            starIndex = getStarIndex(indices[k], input, i);
          }
        }

        const res = parseInt(number);

        if (starIndex) {
          const key = parseInt(starIndex.i.toString() + starIndex.j.toString());
          if (numbers.has(key)) {
            numbers.get(key).push(number);
          } else {
            numbers.set(key, [number]);
          }
        }
        indices = [];
      }
    }
  }

  let res = 0;
  for (let [key, value] of numbers) {
    if (value.length > 1) {
      res += value.reduce((acc, number) => acc * number, 1);
    }
  }

  return res;
};

console.log(part1());
console.log(part2());

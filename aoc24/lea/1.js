const fs = require("fs");

let left = [];
let right = [];

const readInput = (filepath) => {
  const file = fs.readFileSync(filepath, "utf-8");
  file.split(/\r?\n/).forEach((line, index) => {
    res = line.split(/(\s+)/);
    left.push(res[0]);
    right.push(res[res.length - 1]);
  });
};

const part1 = (left, right) => {
  left.sort();
  right.sort();

  return left.reduce(
    (acc, val, idx) => acc + Math.abs(val - right[idx]),
    0
  );
};

const part2 = (left, right) => {
  right.sort();

  return left.reduce(
    (acc, val) => acc + val * right.filter((s) => s === val).length,
    0
  );
};

readInput("./1-puzzle.txt");

console.log(part1(left, right));
console.log(part2(left, right));

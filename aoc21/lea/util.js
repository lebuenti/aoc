const fs = require("fs");
const assert = require("assert");

function readDataAsLine(filePath) {
  const puzzleInput = fs.readFileSync(filePath, {
    encoding: "utf8",
    flag: "r",
  });
  return puzzleInput.split("\n");
}

function readDataAsString(filePath) {
  const puzzleInput = fs.readFileSync(filePath, {
    encoding: "utf8",
    flag: "r",
  });
  return puzzleInput;
}

function numberStrToNumberArr(str) {
  if (!str) {
    return [];
  }
  const splitted = str.split(/\s+/);
  return splitted.reduce((acc, split) => {
    acc.push(parseInt(split, 10));
    return acc;
  }, []);
}

assert.deepEqual(numberStrToNumberArr("35 14 2 3 -7"), [35, 14, 2, 3, -7]);
assert.deepEqual(numberStrToNumberArr("35 14    2 3    -7"), [35, 14, 2, 3, -7]);
assert.deepEqual(numberStrToNumberArr("-7"), [-7]);
assert.deepEqual(numberStrToNumberArr("12345678"), [12345678]);
assert.deepEqual(numberStrToNumberArr(""), []);

module.exports = { readDataAsLine, readDataAsString, numberStrToNumberArr };

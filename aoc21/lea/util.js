const fs = require("fs");

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

module.exports = { readDataAsLine, readDataAsString };

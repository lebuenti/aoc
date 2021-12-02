const fs = require("fs");

function readDataAsLine(filePath) {
  const puzzleInput = fs.readFileSync(filePath, {
    encoding: "utf8",
    flag: "r",
  });
  return puzzleInput.split("\n");
}

module.exports = { readDataAsLine };

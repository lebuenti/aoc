const fs = require("fs");

const part1 = (possible) => {
  let sum = 0;

  const allFileContents = fs.readFileSync("./input.txt", "utf-8");

  allFileContents.split(/\r?\n/).forEach((line) => {
    const gameId = parseInt(line.split(":")[0].match(/(\d+)/)[0]);
    const gameHistory = line.split(":")[1];

    const subsets = gameHistory.split(";");
    let isPossible = true;

    subsets.forEach((subset) => {
      const colors = subset.split(",");

      colors.forEach((c) => {
        const colorNumber = parseInt(c.match(/(\d+)/)[0]);

        if (
          (c.indexOf("blue") >= 0 && colorNumber > possible.blue) ||
          (c.indexOf("red") >= 0 && colorNumber > possible.red) ||
          (c.indexOf("green") >= 0 && colorNumber > possible.green)
        ) {
          isPossible = false;
        }
      });
    });

    if (isPossible) {
      sum += gameId;
    }
  });

  return sum;
};

const part2 = () => {
  let sum = 0;

  const allFileContents = fs.readFileSync("./input.txt", "utf-8");

  allFileContents.split(/\r?\n/).forEach((line) => {
    const gameHistory = line.split(":")[1];
    const subsets = gameHistory.split(";");
    const max = { r: 0, g: 0, b: 0 };

    subsets.forEach((subset) => {
      const colors = subset.split(",");

      colors.forEach((c) => {
        const colorNumber = parseInt(c.match(/(\d+)/)[0]);

        if (c.indexOf("red") >= 0) {
          max.r = max.r < colorNumber ? colorNumber : max.r;
        }
        if (c.indexOf("green") >= 0) {
          max.g = max.g < colorNumber ? colorNumber : max.g;
        }
        if (c.indexOf("blue") >= 0) {
          max.b = max.b < colorNumber ? colorNumber : max.b;
        }
      });
    });

    sum += max.r * max.g * max.b;
  });
  return sum;
};

console.log("part1: ", part1({ red: 12, blue: 14, green: 13 }));
console.log("part2: ", part2());

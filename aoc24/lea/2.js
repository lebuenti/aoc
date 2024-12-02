const fs = require("fs");

let arr = [];

const readInput = (filepath) => {
  const file = fs.readFileSync(filepath, "utf-8");
  file.split(/\r?\n/).forEach((line, index) => {
    res = line.split(/(\s+)/);
    arr.push(res.filter((str) => /\S/.test(str)).map((str) => parseInt(str)));
  });
};

const isUnsafe = (line) => {
  for (let j = 0; j < line.length - 1; j++) {
    const ascending = line.every((x, i) => i === 0 || x > line[i - 1]);
    const descending = line.every((x, i) => i === 0 || x < line[i - 1]);

    if (
      (!ascending && !descending) ||
      Math.abs(line[j + 1] - line[j]) > 3 ||
      Math.abs(line[j + 1] - line[j]) == 0
    ) {
      return true;
    }
  }
  return false;
};

const part1and2 = () => {
  var safeCounter2 = 0;
  var safeCounter1 = 0;

  for (let i = 0; i < arr.length; i++) {
    for (let j = -1; j < arr[i].length; j++) {
      const x = [...arr[i]];
      if (j !== -1) {
        x.splice(j, 1);
      }
      if (!isUnsafe(x)) {
        safeCounter2++;
        if (j === -1) {
          safeCounter1++;
        }
        break;
      }
    }
  }
  return { safeCounter1, safeCounter2 };
};

readInput("./2-input.txt");

console.log(part1and2());

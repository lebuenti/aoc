const fs = require("fs");

var count = 0;
var stop = false;

const readInput = (filepath) => {
  const file = fs.readFileSync(filepath, "utf-8");
  file.split(/\r?\n/).forEach((line) => {
    const result = line.match(/mul\(\d+,\d+\)|don't\(\)|do\(\)/g);

    result.forEach((r) => {
      switch (r) {
        case "don't()":
          stop = true;
          break;
        case "do()":
          stop = false;
          break;
        default:
          if (!stop) {
            const [a, b] = r
              .replaceAll("mul(", "")
              .replaceAll(")", "")
              .split(",");
            count += parseInt(a) * parseInt(b);
          }
          break;
      }
    });
  });
};

readInput("./3-input.txt");

console.log(count);

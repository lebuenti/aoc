const fs = require("fs");

const exampleInput = "./exampleInput01.txt";
const input = "./input01.txt";

const readDataAsLine = (filePath) => {
  const puzzleInput = fs.readFileSync(filePath, {
    encoding: "utf8",
    flag: "r",
  });
  a = [];
  let beginLine = 0;
  for (let i = 0; i < puzzleInput.length; i++) {
    if (puzzleInput[i] === "\n") {
      let line = "";
      for (let j = beginLine; j < i; j++) {
        line += puzzleInput[j];
      }
      a.push(line);
      beginLine = i + 1;
    }
  }
  return a;
};

const part1 = () => {
  const a = readDataAsLine(input);

  let increaseCounter = 0;
  for (let i = 0; i < a.length; i++) {
    if (i != 0 && parseInt(a[i]) > parseInt(a[i - 1])) {
      increaseCounter++;
    }
  }

  console.log("Increase counter part 1: ", increaseCounter);
};

const part2 = () => {
  const puzzleInput = readDataAsLine(input);

  let sums = [];
  for (let i = 0; i < puzzleInput.length - 2; i++) {
    let sum =
      parseInt(puzzleInput[i]) +
      parseInt(puzzleInput[i + 1]) +
      parseInt(puzzleInput[i + 2]);
    sums.push(sum);
  }

  let increaseCounter = 0;
  for (let i = 0; i < sums.length; i++) {
    if (i != 0 && sums[i] > sums[i - 1]) {
      increaseCounter++;
    }
  }
  console.log("Increase counter part 2: " + increaseCounter);
};

part1();
part2();

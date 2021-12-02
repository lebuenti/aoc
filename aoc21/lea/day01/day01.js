const readDataAsLine = require("../util");

const exampleInput = "./day01/exampleInput01.txt";
const input = "./day01/input01.txt";

const part1 = () => {
  const a = readDataAsLine.readDataAsLine(input);

  let increaseCounter = 0;
  for (let i = 0; i < a.length; i++) {
    if (i != 0 && parseInt(a[i]) > parseInt(a[i - 1])) {
      increaseCounter++;
    }
  }

  console.log("Increase counter part 1: ", increaseCounter);
};

const part2 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);

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

const readDataAsLine = require("../util");

const exampleInput = "./exampleInput.txt";
const input = "./input.txt";

const part1 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);
  let depth = 0;
  let horizontal = 0;

  puzzleInput.forEach((elem) => {
    let tmp = elem.split(" ");
    let directory = tmp[0];
    let steps = parseInt(tmp[1]);

    if (directory === "forward") {
      horizontal += steps;
    } else if (directory === "down") {
      depth += steps;
    } else if (directory === "up") {
      depth -= steps;
    }
  });

  console.log("Horizontal: ", horizontal);
  console.log("depth: ", depth);
  console.log("mult: ", horizontal * depth);
};

const part2 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);
  let depth = 0;
  let horizontal = 0;
  let aim = 0;

  puzzleInput.forEach((elem) => {
    let tmp = elem.split(" ");
    let directory = tmp[0];
    let steps = parseInt(tmp[1]);

    if (directory === "forward") {
      horizontal += steps;
      depth += steps * aim;
    } else if (directory === "down") {
      aim += steps;
    } else if (directory === "up") {
      aim -= steps;
    }
  });

  console.log("Horizontal: ", horizontal);
  console.log("depth: ", depth);
  console.log("aim: ", aim);
  console.log("mult: ", horizontal * depth);
};

part1();
console.log("\n");
part2();

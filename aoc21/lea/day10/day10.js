const readDataAsLine = require("../util");

const exampleInput = "./lea/day10/exampleInput.txt";
const input = "./lea/day10/input.txt";

const isClosedBracket = (current) => {
  return (
    current === ")" || current === "}" || current === "]" || current === ">"
  );
};

const isCorrectPair = (open, close) => {
  switch (open) {
    case "(":
      return close === ")";
    case "{":
      return close === "}";
    case "[":
      return close === "]";
    case "<":
      return close === ">";
  }
};

const getClosingBracket = (open) => {
  switch (open) {
    case "(":
      return ")";
    case "{":
      return "}";
    case "[":
      return "]";
    case "<":
      return ">";
  }
};

const calculateIllegalCharScore = (bracket) => {
  switch (bracket) {
    case ")":
      return 3;
    case "}":
      return 1197;
    case "]":
      return 57;
    case ">":
      return 25137;
  }
};

const part1 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);

  let score = 0;

  puzzleInput.forEach((line) => {
    for (let i = 0; i < line.length - 1; i++) {
      if (isCorrectPair(line[i], line[i + 1])) {
        line = line.slice(0, i, i + 1) + line.slice(i + 2);
        i -= 2;
      } else if (!isClosedBracket(line[i]) && isClosedBracket(line[i + 1])) {
        score += calculateIllegalCharScore(line[i + 1]);
        return;
      }
    }
  });

  console.log("Illegal character score: ", score);
};

const part2 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);

  const points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
  };
  let scores = [];

  puzzleInput.forEach((line) => {
    for (let i = 0; i < line.length - 1; i++) {
      if (isCorrectPair(line[i], line[i + 1])) {
        line = line.slice(0, i, i + 1) + line.slice(i + 2);
        i -= 2;
      } else if (!isClosedBracket(line[i]) && isClosedBracket(line[i + 1])) {
        return;
      }
    }
    let autocomplete = [];
    for (let i = line.length - 1; i >= 0; i--) {
      autocomplete.push(getClosingBracket(line[i]));
    }
    let score = 0;
    autocomplete.forEach((bracket) => {
      score *= 5;
      score += points[bracket];
    });
    scores.push(score);
  });
  scores.sort((a, b) => {
    return a - b;
  });
  console.log("Autocomplete score: ", scores[Math.floor(scores.length / 2)]);
};

part1();
part2();

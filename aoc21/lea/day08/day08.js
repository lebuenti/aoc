const readDataAsLine = require("../util");
const exampleInput = "./lea/day08/exampleInput.txt";
const input = "./lea/day08/input.txt";

const part1 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);

  let amountUnique = 0;
  puzzleInput.forEach((line) => {
    const splitted = line.split(" | ");
    const outputValues = splitted[1].split(" ");
    outputValues.forEach((val) => {
      if (
        val.length === 2 ||
        val.length === 4 ||
        val.length === 3 ||
        val.length === 7
      ) {
        amountUnique++;
      }
    });
  });

  console.log(amountUnique);
};

const includesOtherNumber = (value, number) => {
  let includesNumber = true;
  for (let char of number) {
    if (!value.includes(char)) {
      includesNumber = false;
    }
  }
  return includesNumber;
};

const isNumber = (value, number) => {
  if (value.length !== number.length) return false;
  return includesOtherNumber(value, number);
};

const includesThreeCharsOfNumber = (value, four) => {
  let counter = 0;
  for (let char of four) {
    if (value.includes(char)) {
      counter++;
    }
  }
  return counter === 3;
};

const part2 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);

  let result = 0;

  puzzleInput.forEach((line) => {
    const splitted = line.split(" | ");
    const outputValues = splitted[1].split(" ");
    let numbers = splitted[0].split(" ");

    const decodedNum = new Array(10);
    decodedNum[1] = numbers.find((val) => val.length === 2);
    decodedNum[4] = numbers.find((val) => val.length === 4);
    decodedNum[7] = numbers.find((val) => val.length === 3);
    decodedNum[8] = numbers.find((val) => val.length === 7);

    numbers.forEach((n) => {
      if (n.length === 6) {
        if (!includesOtherNumber(n, decodedNum[1])) {
          decodedNum[6] = n;
        } else if (includesOtherNumber(n, decodedNum[4])) {
          decodedNum[9] = n;
        } else {
          decodedNum[0] = n;
        }
      } else if (n.length === 5) {
        if (
          includesThreeCharsOfNumber(n, decodedNum[4]) &&
          includesOtherNumber(n, decodedNum[1])
        ) {
          decodedNum[3] = n;
        } else if (
          includesThreeCharsOfNumber(n, decodedNum[4]) &&
          !includesOtherNumber(n, decodedNum[1])
        ) {
          decodedNum[5] = n;
        } else {
          decodedNum[2] = n;
        }
      }
    });

    let tmp = "";
    outputValues.forEach((ov) => {
      for (let i = 0; i < decodedNum.length; i++) {
        if (isNumber(ov, decodedNum[i])) {
          tmp += i.toString();
          break;
        }
      }
    });
    result += parseInt(tmp);
  });

  console.log(result);
};

part1();
part2();

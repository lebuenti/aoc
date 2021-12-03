const readDataAsLine = require("../util");

const exampleInput = "./lea/day03/exampleInput.txt";
const input = "./lea/day03/input.txt";

const binaryArrayToString = (array) => {
  let result = "";
  for (let i = 0; i < array.length; i++) {
    result += array[i];
  }
  return result;
};

const part1 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);

  const a = [];
  for (let i = 0; i < puzzleInput.length; i++) {
    a.push([...puzzleInput[i]]);
  }

  let gammaRate = "";
  for (let j = 0; j < a[0].length; j++) {
    let zeroCounter = 0;
    let oneCounter = 0;

    for (let i = 0; i < a.length; i++) {
      if (parseInt(a[i][j]) === 0) zeroCounter++;
      else if (parseInt(a[i][j]) === 1) oneCounter++;
    }

    if (zeroCounter > oneCounter) gammaRate += "0";
    else if (oneCounter > zeroCounter) gammaRate += "1";
    else console.log("zeroCounter and oneCounter is eqaual");
  }

  let epsilonRate = "";
  for (let i = 0; i < gammaRate.length; i++) {
    if (gammaRate.charAt(i) === "0") epsilonRate += "1";
    else if (gammaRate.charAt(i) === "1") epsilonRate += "0";
  }

  console.log("Part1: ", parseInt(gammaRate, 2) * parseInt(epsilonRate, 2));
};

const oxygenGenerator = (position, a) => {
  if (a.length === 1) {
    return [a[0]];
  }

  let ones = [];
  let nulls = [];
  for (let i = 0; i < a.length; i++) {
    if (parseInt(a[i][position]) === 0) {
      nulls.push(a[i]);
    } else if (parseInt(a[i][position]) === 1) {
      ones.push(a[i]);
    }
  }

  if (ones.length === nulls.length) {
    return ones;
  } else {
    return ones.length > nulls.length ? ones : nulls;
  }
};

const co2ScrubberRating = (position, a) => {
  if (a.length === 1) {
    return [a[0]];
  }

  let ones = [];
  let nulls = [];
  for (let i = 0; i < a.length; i++) {
    if (parseInt(a[i][position]) === 0) {
      nulls.push(a[i]);
    } else if (parseInt(a[i][position]) === 1) {
      ones.push(a[i]);
    }
  }
  if (ones.length === nulls.length) {
    return nulls;
  } else {
    return ones.length > nulls.length ? nulls : ones;
  }
};

const part2 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);
  const a = [];
  for (let i = 0; i < puzzleInput.length; i++) {
    a.push([...puzzleInput[i]]);
  }

  let oxygenNumbers = [...a];
  for (let i = 0; oxygenNumbers.length > 1; i++) {
    oxygenNumbers = oxygenGenerator(i, oxygenNumbers);
  }

  let co2ScrubberRatingNumbers = [...a];
  for (let i = 0; co2ScrubberRatingNumbers.length > 1; i++) {
    co2ScrubberRatingNumbers = co2ScrubberRating(i, co2ScrubberRatingNumbers);
  }

  console.log(
    "Part2: ",
    parseInt(binaryArrayToString(oxygenNumbers[0]), 2) *
      parseInt(binaryArrayToString(co2ScrubberRatingNumbers[0]), 2)
  );
};

part1();
part2();

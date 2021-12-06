const readDataAsString = require("../util");

const exampleInput = "./lea/day06/exampleInput.txt";
const input = "./lea/day06/input.txt";

const solution = (days) => {
  const puzzleInput = readDataAsString.readDataAsString(input);
  const fishes = puzzleInput.split(",").map((elem) => parseInt(elem));

  let fishCounter = [
    fishes.filter((elem) => elem === 0).length,
    fishes.filter((elem) => elem === 1).length,
    fishes.filter((elem) => elem === 2).length,
    fishes.filter((elem) => elem === 3).length,
    fishes.filter((elem) => elem === 4).length,
    fishes.filter((elem) => elem === 5).length,
    fishes.filter((elem) => elem === 6).length,
    fishes.filter((elem) => elem === 7).length,
    fishes.filter((elem) => elem === 8).length,
  ];

  //                                           0 1 2 3 4 5 6 7 8
  //                                           -----------------
  //amount fishes                              0 1 1 2 1 0 0 0 0
  //shift + a[6] = leftElem & a[8] = leftElem  1 1 2 1 0 0 0 0 0
  //shift + a[6] = leftElem & a[8] = leftElem  1 2 1 0 0 0 1 0 1
  //shift + a[6] = leftElem & a[8] = leftElem  2 1 0 0 0 1 1 1 1

  for (let day = 1; day <= days; day++) {
    let leftFish = fishCounter.shift();
    fishCounter[6] += leftFish;
    fishCounter[8] = leftFish;
  }

  let res = 0;
  fishCounter.forEach((fish) => {
    res += fish;
  });

  console.log(res);
};

console.log("part1: ");
solution(80);
console.log("part2: ");
solution(256);

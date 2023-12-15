const fs = require("fs");
const { numberStrToNumberArr } = require("../../../aoc21/lea/util");

const file = fs.readFileSync("./input.txt", "utf-8");

const calculateAmountOfWins = (maxTime, maxDistance) => {
  let wincounter = 0;
  for (let j = 1; j <= maxTime; j++) {
    const millimeters = (maxTime - j) * j;
    if (millimeters > maxDistance) {
      wincounter++;
    }
  }
  return wincounter;
};

const part1 = () => {
  const times = numberStrToNumberArr(
    file.split(/\r?\n/)[0].split("Time:")[1].trim()
  );
  const distances = numberStrToNumberArr(
    file.split(/\r?\n/)[1].split("Distance:")[1].trim()
  );

  return times.reduce((acc, time, index) => {
    const wincounter = calculateAmountOfWins(time, distances[index]);
    return wincounter > 0 ? (acc *= wincounter) : acc;
  }, 1);
};

const part2 = () => {
  const times = numberStrToNumberArr(
    file.split(/\r?\n/)[0].split("Time:")[1].replace(/ /g, "")
  );
  const distances = numberStrToNumberArr(
    file.split(/\r?\n/)[1].split("Distance:")[1].replace(/ /g, "")
  );
  return calculateAmountOfWins(times[0], distances[0]);
};

console.log(part1());
console.log(part2());

const readDataAsString = require("../util");

const exampleInput = "./lea/day07/exampleInput.txt";
const input = "./lea/day07/input.txt";

const part1 = () => {
  const puzzleInput = readDataAsString.readDataAsString(exampleInput);
  const data = puzzleInput.split(",").map((elem) => parseInt(elem));

  let max = Math.max(...data);
  let minFuel = { fuel: undefined, position: 0 };

  for (let i = 0; i <= max; i++) {
    let currentFuel = 0;

    data.forEach((d) => {
      let tmp = i - d;
      if (tmp < 0) tmp = tmp * -1;
      currentFuel += tmp;
    });
    if (!minFuel.fuel || currentFuel < minFuel.fuel) {
      minFuel.fuel = currentFuel;
      minFuel.position = i;
    }
  }

  console.log("Max: ", minFuel.fuel, ", pos: ", minFuel.position);
};

const part2 = () => {
  const puzzleInput = readDataAsString.readDataAsString(input);
  const data = puzzleInput.split(",").map((elem) => parseInt(elem));

  let max = Math.max(...data);
  let minFuel = { fuel: undefined, position: 0 };

  for (let pos = 0; pos <= max; pos++) {
    let currentFuel = 0;

    data.forEach((crabPos) => {
      let steps = pos - crabPos;
      if (steps < 0) steps = steps * -1;

      for (let j = 0; j <= steps; j++) {
        currentFuel += j;
      }
    });
    if (!minFuel.fuel || currentFuel < minFuel.fuel) {
      minFuel.fuel = currentFuel;
      minFuel.position = pos;
    }
  }

  console.log("Max: ", minFuel.fuel, ", pos: ", minFuel.position);
};

part1();
part2();

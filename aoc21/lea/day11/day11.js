const readDataAsLine = require("../util");
const exampleInput = "./lea/day11/exampleInput.txt";
const input = "./lea/day11/input.txt";

let flashCounter = 0;

const createMatrix = (puzzleInput) => {
  let matrix = [];
  puzzleInput.forEach((line) => {
    let tmp = [];
    for (let i = 0; i < line.length; i++) {
      tmp.push(parseInt(line.charAt(i)));
    }
    matrix.push(tmp);
  });
  return matrix;
};

const flash = (matrix, i, j) => {
  for (let k = i - 1; k <= i + 1; k++) {
    if (k < 0) continue;
    if (k >= matrix.length) continue;

    for (let l = j - 1; l <= j + 1; l++) {
      if (l < 0 || l >= matrix[k].length || (i == k && j == l)) continue;
      if (matrix[k][l] !== 0) {
        matrix[k][l]++;
      }
      if (matrix[k][l] > 9) {
        matrix[k][l] = 0;
        flashCounter++;
        matrix = flash(matrix, k, l);
      }
    }
  }

  return matrix;
};

const flashMatrix = (matrix) => {
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (matrix[i][j] > 9) {
        matrix[i][j] = 0;
        flashCounter++;
        matrix = flash(matrix, i, j);
      }
    }
  }
  return matrix;
};

const isSynchron = (matrix) => {
  let first = matrix[0][0];
  for (let line of matrix) {
    for (let i = 0; i < line.length; i++) {
      if (line[i] !== first) {
        return false;
      }
    }
  }
  return true;
};

const part1 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);
  let matrix = createMatrix(puzzleInput);

  let counter = 1;
  while (true) {
    for (let i = 0; i < matrix.length; i++) {
      for (let j = 0; j < matrix[i].length; j++) {
        matrix[i][j]++;
      }
    }
    matrix = flashMatrix(matrix);
    if (isSynchron(matrix)) {
      break;
    }
    counter++;
  }
  console.log("flashcounter:", flashCounter);
  console.log("step synchron:", counter);
};

part1();

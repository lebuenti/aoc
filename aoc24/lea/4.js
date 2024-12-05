const fs = require("fs");

const matrix = [];

const readInput = (filepath) => {
  const file = fs.readFileSync(filepath, "utf-8");
  file.split(/\r?\n/).forEach((line) => {
    matrix.push([...line]);
  });
};

readInput("./4-input.txt");

const rows = matrix.length;
const cols = matrix[0].length;

const search = (dx, dy, x, y, word) => {
  const path = [];
  for (let k = 1; k < word.length; k++) {
    const newX = x + k * dx;
    const newY = y + k * dy;

    if (
      !(
        newX >= 0 &&
        newX < rows &&
        newY >= 0 &&
        newY < cols &&
        matrix[newX][newY] === word[k]
      )
    ) {
      return null;
    }
    path.push([newX, newY]);
  }
  return path;
};

const riddle = (str, directions) => {
  const word = [...str];

  let wordCounter = 0;
  const paths = [];

  for (let x = 0; x < rows; x++) {
    for (let y = 0; y < cols; y++) {
      if (matrix[x][y] === word[0]) {
        directions.forEach(([dx, dy]) => {
          const path = search(dx, dy, x, y, word);
          if (path) {
            wordCounter++;
            paths.push(path);
          }
        });
      }
    }
  }
  return { wordCounter, paths };
};

console.log(
  "XMAS",
  riddle("XMAS", [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1],
  ]).wordCounter
);

var paths = riddle("MAS", [
  [-1, -1],
  [-1, 1],
  [1, -1],
  [1, 1],
]);

// ty chatgtp for this rest filter stuff
const countMap = {};
paths.paths.forEach(([first]) => {
  const key = JSON.stringify(first);
  countMap[key] = (countMap[key] || 0) + 1;
});

const duplicates = paths.paths.filter(
  ([first]) => countMap[JSON.stringify(first)] > 1
);

console.log("X-MAS", duplicates.length / 2);

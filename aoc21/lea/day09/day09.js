const readDataAsLine = require("../util");
const exampleInput = "./lea/day09/exampleInput.txt";
const input = "./lea/day09/input.txt";

const part1 = (inp) => {
  const puzzleInput = readDataAsLine.readDataAsLine(inp);

  let smallest = [];
  for (let i = 0; i < puzzleInput.length; i++) {
    for (let j = 0; j < puzzleInput[i].length; j++) {
      let exists = [ i - 1 >= 0, i + 1 < puzzleInput.length, j - 1 >= 0, j + 1 < puzzleInput[i].length];

      let checks = [ i - 1 >= 0 && puzzleInput[i][j] < puzzleInput[i - 1][j],
        i + 1 < puzzleInput.length && puzzleInput[i][j] < puzzleInput[i + 1][j],
        j - 1 >= 0 && puzzleInput[i][j] < puzzleInput[i][j - 1],
        j + 1 < puzzleInput[i].length && puzzleInput[i][j] < puzzleInput[i][j + 1],
      ];

      let error = false;
      for (let k = 0; k < 4; k++) {
        if (exists[k] && !checks[k]) {
          error = true;
        }
      }
      if (!error) smallest.push({ x: j, y: i, val: puzzleInput[i][j] });
    }
  }
  return smallest;
};

const basin = (puzzleInput, lowPoint, points) => {
  if ( lowPoint.x - 1 >= 0 && 
    parseInt(puzzleInput[lowPoint.y][lowPoint.x - 1]) > parseInt(lowPoint.val) &&
    parseInt(puzzleInput[lowPoint.y][lowPoint.x - 1]) < 9) {
    const nextLowPoint = { x: lowPoint.x - 1, y: lowPoint.y, val: puzzleInput[lowPoint.y][lowPoint.x - 1] };
    if (! points.find(obj => obj.x === nextLowPoint.x && obj.y === nextLowPoint.y)) {
        points.push(nextLowPoint);
        basin(puzzleInput, nextLowPoint, points);
    }
  }

  if ( lowPoint.x + 1 < puzzleInput[lowPoint.y].length && 
    parseInt(puzzleInput[lowPoint.y][lowPoint.x + 1]) > parseInt(lowPoint.val)&&
    parseInt(puzzleInput[lowPoint.y][lowPoint.x + 1]) < 9 ) {
    const nextLowPoint = { x: lowPoint.x + 1, y: lowPoint.y, val: puzzleInput[lowPoint.y][lowPoint.x + 1]};
    if (! points.find(obj => obj.x === nextLowPoint.x && obj.y === nextLowPoint.y)) {
        points.push(nextLowPoint);
        basin(puzzleInput, nextLowPoint, points);
    }
  }

  if ( lowPoint.y - 1 >= 0 && 
    parseInt(puzzleInput[lowPoint.y - 1][lowPoint.x]) > parseInt(lowPoint.val) &&
    parseInt(puzzleInput[lowPoint.y - 1][lowPoint.x]) < 9 ) {
    const nextLowPoint = { x: lowPoint.x, y: lowPoint.y - 1, val: puzzleInput[lowPoint.y - 1][lowPoint.x] };
    if (! points.find(obj => obj.x === nextLowPoint.x && obj.y === nextLowPoint.y)) {
        points.push(nextLowPoint);
        basin(puzzleInput, nextLowPoint, points);
    }
  }

  if ( lowPoint.y + 1 < puzzleInput.length && 
    parseInt(puzzleInput[lowPoint.y + 1][lowPoint.x]) > parseInt(lowPoint.val)  &&
    parseInt(puzzleInput[lowPoint.y + 1][lowPoint.x]) < 9 ) {
    const nextLowPoint = { x: lowPoint.x, y: lowPoint.y + 1, val: puzzleInput[lowPoint.y + 1][lowPoint.x] };
    if (! points.find(obj => obj.x === nextLowPoint.x && obj.y === nextLowPoint.y)) {
        points.push(nextLowPoint);
        basin(puzzleInput, nextLowPoint, points);
    }
  }

  
  return points;
};

const part2 = (inp) => {
  const lowPoints = part1(inp);
  let puzzleInput = readDataAsLine.readDataAsLine(inp);
  const sizesOfBasins = [];

  lowPoints.forEach((lowPoint) => {
    const points = basin(puzzleInput, lowPoint, []);
    sizesOfBasins.push(points.length + 1);

    for (let p of points) {
        let s = puzzleInput[p.y];
        let  c = s.split('');
        c[p.x] = '9';
        s = c.join('');
        puzzleInput[p.y ] = s;
    };
  });

  sizesOfBasins.sort((a, b) => b - a);
  console.log(sizesOfBasins);
  console.log(sizesOfBasins[0] * sizesOfBasins[1] * sizesOfBasins[2]);
};

//part 1
const lowPoints = part1(input);
const riskLevel = lowPoints.map((val) => ++val.val);
let sum = riskLevel.reduce((pv, cv) => pv + cv, 0);
console.log(sum);

//part 2
part2(input);

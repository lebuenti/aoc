const readDataAsLine = require("../util");

const exampleInput = "./lea/day05/exampleInput.txt";
const input = "./lea/day05/input.txt";

const findMax = (points) => {
  let res = Math.max(...points.map(o => o.from.x));
  let res2 = Math.max(...points.map(o => o.to.x));
  let res3 = Math.max(...points.map(o => o.from.y));
  let res4 = Math.max(...points.map(o => o.to.y));
  return { x: res > res2 ? res : res2, y: res3 > res4 ? res3 : res4 };
};

const printCard = (card) => {
  card.forEach((row) => {
    row.forEach((cell) => {
      if (cell === 0) {
        process.stdout.write(".");
      } else {
        process.stdout.write(cell.toString());
      }
    });
    console.log("\n");
  });
};

const createPointArray = (puzzleInput, withDiagonal = false) => {
  let points = [];
  puzzleInput.forEach((input) => {
    const splitted = input.split("->");
    const from = splitted[0].split(",");
    const to = splitted[1].split(",");

    let point = {
      from: { x: parseInt(from[0]), y: parseInt(from[1]) },
      to: { x: parseInt(to[0]), y: parseInt(to[1]) },
    };

    if (!withDiagonal && (point.from.y === point.to.y || point.from.x === point.to.x)) {
      points.push(point);
    } else if (withDiagonal) {
      points.push(point);
    }
  });
  return points;
};

const getPointsBetween = (p1, p2) => {
  let res = [];

  if (p1.x > p2.x) {
    for (let i = p1.x, c = 0; i >= p2.x; i--, c++) {
      if (p1.y < p2.y) {
        res.push({ x: i, y: p1.y + c });
      } else if (p1.y === p2.y) {
        res.push({ x: i, y: p1.y });
      } else {
        res.push({ x: i, y: p1.y - c });
      }
    }
  } else if (p1.x === p2.x) {
    if (p1.y < p2.y) {
      for (let i = p1.y; i <= p2.y; i++) {
        res.push({ x: p1.x, y: i });
      }
    } else {
      for (let i = p2.y; i <= p1.y; i++) {
        res.push({ x: p1.x, y: i });
      }
    }
  } else if (p1.x < p2.x) {
    for (let i = p1.x, c = 0; i <= p2.x; i++, c++) {
      if (p1.y < p2.y) {
        res.push({ x: i, y: p1.y + c });
      } else if (p1.y === p2.y) {
        res.push({ x: i, y: p1.y });
      } else {
        res.push({ x: i, y: p1.y - c });
      }
    }
  }

  return res;
};

const solution = (diagonal) => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);
  const points = createPointArray(puzzleInput, diagonal);

  const max = findMax(points);
  let card = [];
  for (let y = 0; y <= max.y; y++) {
    let row = [];
    for (let x = 0; x <= max.x; x++) {
      row.push(0);
    }
    card.push(row);
  }
  points.forEach((point) => {
    const pointsBetween = getPointsBetween(point.from, point.to);
    pointsBetween.forEach((p) => {
      card[p.y][p.x] = card[p.y][p.x] + 1;
    });
  });

  printCard(card);

  let count = 0;
  card.forEach((row) => {
    count += row.filter((cell) => cell > 1).length;
  });

  console.log(count);
};

//part1
console.log("part1:");
solution(false);
console.log("part2:");
//part2
solution(true);

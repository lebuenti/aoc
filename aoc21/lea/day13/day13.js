const readDataAsLine = require("../util");
const exampleInput = "./lea/day13/exampleInput.txt";
const input = "./lea/day13/input.txt";

const getMax = (array) => {
  let maxX = 0;
  let maxY = 0;
  array.forEach((row) => {
    if (row[0] > maxX) maxX = row[0];
    if (row[1] > maxY) maxY = row[1];
  });

  return { x: maxX, y: maxY };
};

const printPaper = (paper) => {
  paper.forEach((line) => {
    line.forEach((c) => {
      process.stdout.write(c);
    });
    console.log("");
  });
  console.log("");
};

const part1 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);

  let coordinates = [];
  let foldInstructions = [];
  puzzleInput.forEach((input) => {
    if (!input.includes("fold along") && input !== "") {
      let tmp = input.split(",");
      tmp[0] = parseInt(tmp[0]);
      tmp[1] = parseInt(tmp[1]);
      coordinates.push(tmp);
    } else if (input.includes("fold along") && input !== "") {
      foldInstructions.push(input);
    }
  });

  const { x, y } = getMax(coordinates);
  let paper = [];

  for (let i = 0; i <= y; i++) {
    let tmp = [];
    for (let j = 0; j <= x; j++) {
      tmp.push(".");
    }
    paper.push(tmp);
  }

  coordinates.forEach((c) => {
    paper[c[1]][c[0]] = "#";
  });

  foldInstructions.forEach((fi) => {
    const s = fi.split("=");
    const number = s[1];
    const direction = s[0].charAt(s[0].length - 1);

    if (direction === "y") {
      let deleted = paper.splice(number);
      deleted.splice(0, 1);

      deleted.reverse();
      for (let j = 0; j < deleted.length; j++) {
        for (let i = 0; i < deleted[j].length; i++) {
          if (deleted[j][i] === "#") {
            paper[Math.abs(j - deleted.length + 1)][i] = deleted[j][i];
            paper[number - deleted.length + j][i] = deleted[j][i];
          }
        }
      }
    } else {
      for (let j = 0; j < paper.length; j++) {
        const deleted = paper[j].splice(number);
        deleted.splice(0, 1);
        deleted.reverse();
        for (let i = 0; i < deleted.length; i++) {
          if (deleted[i] === "#") {
            paper[j][number - deleted.length + i] = deleted[i];
          }
        }
      }
    }
  });

  printPaper(paper);

  let counter = 0;
  paper.forEach((line) => {
    line.forEach((c) => {
      if (c === "#") counter++;
    });
  });
  console.log(counter);
};

part1();

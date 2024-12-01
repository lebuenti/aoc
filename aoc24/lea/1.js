const fs = require("fs");

let left = [];
let right = [];

const readInput = (filepath) => {
  const file = fs.readFileSync(filepath, "utf-8");
  file.split(/\r?\n/).forEach((line, index) => {
    res = line.split(/(\s+)/);
    left.push(res[0]);
    right.push(res[res.length - 1]);
  });
};

const part1 = (left, right) => {
  left.sort();
  right.sort();

  let sumd = 0;

  for (let i = 0; i < left.length; i++) {
    sumd += Math.abs(left[i] - right[i]);
  }
  return sumd;
};

const part2 = (left, right) => {
    right.sort();

    let sumM = 0;
    
    left.forEach(f => {
        let amount = right.filter(s => s === f).length;
        sumM += f * amount;
    });

    return sumM;
}

readInput("./1-puzzle.txt");

console.log(part1(left, right));
console.log(part2(left, right));

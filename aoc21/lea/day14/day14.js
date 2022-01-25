const readDataAsLine = require("../util");
const exampleInput = "./lea/day14/exampleInput.txt";
const input = "./lea/day14/input.txt";

const solution = (maxStep) => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);

  let polymer = puzzleInput[0];
  const rules = [...puzzleInput];
  rules.splice(0, 2);

  let counter = new Map();
  let pairs = new Map();
  for (let i = 0; i < polymer.length; i++) {
    if (i + 1 < polymer.length) {
      let pair = polymer[i] + polymer[i + 1];
      pairs.set(pair, (pairs.get(pair) || 0) + 1);
    }
    counter.set(polymer[i], 1 + (counter.get(polymer[i]) || 0));
  }

  for (let step = 1; step <= maxStep; step++) {
    let tmpMap = new Map();

    for (let [pair, amount] of pairs) {
      const rule = rules.find(
        (rule) => rule.charAt(0) + rule.charAt(1) === pair
      );

      const char = rule.charAt(rule.length - 1);
      const a = pair[0] + char;
      const b = char + pair[1];

      tmpMap.set(a, amount + (tmpMap.get(a) || 0));
      tmpMap.set(b, amount + (tmpMap.get(b) || 0));

      counter.set(char, amount + (counter.get(char) || 0));
    }

    pairs = tmpMap;
  }

  let counts = [];
  for (let [char, amount] of counter) {
    counts[char] = amount;
  }

  const max = Object.keys(counts).reduce((a, b) =>
    counts[a] > counts[b] ? a : b
  );
  const min = Object.keys(counts).reduce((a, b) =>
    counts[a] < counts[b] ? a : b
  );
  console.log(counts[max] - counts[min]);
};

solution(10);
solution(40);

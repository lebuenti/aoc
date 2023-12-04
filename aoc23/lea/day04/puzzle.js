const { readDataAsLine } = require("../../../aoc21/lea/util");

const calcWinningNums = (input) => {
  return input.reduce((acc, line) => {
    const winNumS = line
      .split(":")[1]
      .split("|")[0]
      .trim()
      .replace(/\s+/g, ",");
    const numbersS = line
      .split(":")[1]
      .split("|")[1]
      .trim()
      .replace(/\s+/g, ",");

    const winNum = winNumS.split(",").map((item) => parseInt(item, 10));
    const numbers = numbersS.split(",").map((item) => parseInt(item, 10));

    acc.push(numbers.filter((num) => winNum.includes(num)));
    return acc;
  }, []);
};

const part1 = () => {
  const input = readDataAsLine("./input.txt");

  const numbersAndEmpty = calcWinningNums(input);

  const numbers = numbersAndEmpty.filter((wn) => wn.length > 0);

  return numbers.reduce((acc, winNums) => {
    acc += winNums.length === 1 ? 1 : Math.pow(2, winNums.length - 1);
    return acc;
  }, 0);
};

const part2 = () => {
  const input = readDataAsLine("./input.txt");

  const numbers = calcWinningNums(input);

  const amountCards = new Map();

  numbers.forEach((_, index) => {
    amountCards.set(index, 1);
  });

  numbers.forEach((num, i) => {
    const currentAmount = amountCards.get(i) || 0;

    Array.from({ length: currentAmount }).forEach(() => {
      num.forEach((_, k) => {
        const nextIndex = i + 1 + k;
        amountCards.set(nextIndex, (amountCards.get(nextIndex) ?? 0) + 1);
      });
    });
  });

  return [...amountCards.values()].reduce((sum, value) => sum + value, 0);
};

console.log(part1());
console.log(part2());
